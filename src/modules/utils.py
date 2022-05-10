from PyQt5.QtCore import QObject, pyqtSignal
from pathlib import Path
from nptdms import TdmsFile
import numpy as np


def file_valid(file_path: str) -> bool:
    """Determining if the file is in a valid path and has the correct format. i.e. tdms.

    Args:
        file_path (str): File path string.

    Returns:
        bool: True if path is valid and False if not.
    """
    path = Path(file_path)
    if path.is_file():
        if path.suffix == ".tdms":
            return True
    else:
        return False


def assess_paths(source_file: str, destination_path: str) -> str:
    """Assess whether the source and destination paths in the browser text boxes are valid.

    Args:
        source_file (str): Path to the source file.
        destination_path (str): The destination directory.

    Returns:
        str: Appropriate string according to the path assessment.
    """
    if not file_valid(source_file) and not Path(destination_path).is_dir():
        return "Both source and destination are invalid."
    elif not file_valid(source_file):
        return "Source file is not valid."
    elif not Path(destination_path).is_dir():
        return "Destination path is not valid."
    else:
        return ""


def construct_destination_file_path(
    destination_dir: str,
    source_file_path: str,
    destination_file_format: str,
    group_name: str,
) -> str:
    """Construct destination file path based on where the .tdms file is. The destination file (converted file) will have the same name as the source .tdms file.

    Args:
        destination_dir (str): Destination directory.
        source_file_path (str): Source file path.
        destination_file_format (str): Destination file format. i.e. csv
        group_name (str): Group name of the groups inside the .tdms files.

    Returns:
        str: _description_
    """
    destination_file_name = (
        f"{Path(source_file_path).stem}_{group_name}.{destination_file_format}"
    )
    return f"{Path(destination_dir)/destination_file_name}"


class Worker(QObject):
    """Worker object for running the .tdms conversion using threads to prevent the app from hanging."""

    conversion_finished = pyqtSignal()
    conversion_failed = pyqtSignal()
    conversion_progress = pyqtSignal(int)
    conversion_group = pyqtSignal(str)
    cancel_finished = pyqtSignal()

    def tdms_convertor(
        self,
        source_file_path: str,
        destination_dir: str,
    ) -> None:
        """Function for converting the .tdms file.

        Args:
            source_file_path (str): Path to the source file.
            destination_dir (str): Destination directory.
        """
        try:
            with TdmsFile.open(source_file_path) as tdms_file:
                for group in tdms_file.groups():
                    self.conversion_group.emit(group.name)
                    group_df = group.as_dataframe()
                    segments = np.array_split(group_df.index, 101)

                    for count, chunk in enumerate(segments):
                        if count == 0:
                            group_df.loc[chunk].to_csv(
                                construct_destination_file_path(
                                    destination_dir, source_file_path, "csv", group.name
                                ),
                                sep=",",
                                mode="w",
                                index=True,
                            )
                        else:
                            group_df.loc[chunk].to_csv(
                                construct_destination_file_path(
                                    destination_dir, source_file_path, "csv", group.name
                                ),
                                header=None,
                                sep=",",
                                mode="a",
                                index=True,
                            )
                        self.conversion_progress.emit(count)
            self.conversion_finished.emit()
        except:
            self.conversion_failed.emit()
