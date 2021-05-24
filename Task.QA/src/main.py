import os
import xml.etree.ElementTree as ET
import shutil

from typing import List
from src.constants import Path


def read_xml_file(xml_path: str) -> List:
    """
        Read file format xml and returns dictionary path of file

        Parameters
        ----------
        xml_path : str
            Name of file
        Returns
        -------
        tags: List
            Names of path and file
    """

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        tags = []

        for child in root:
            tags.append(child.attrib)

        return tags

    except IOError as e:
        print(e)


def analyze_data() -> bool:
    """
        Read file format xml and returns name data

        Parameters
        ----------
        Returns
        -------
        True: bool
            Answer - whether the copy was successful

    """

    path_to_file = Path.PATH_TO_PROGRAM + Path.DATA_DIRECTORY
    files_list = os.listdir(path_to_file)

    for file in files_list:
        copy_file(read_xml_file(path_to_file + file))

    return True


def copy_file(list) -> None:
    """
        Copying file based on data from xml file

        Parameters
        ----------
        list : List
             Names of path and file
        Returns
        -------
    """

    try:
        if list is not None:
            for dict in list:
                shutil.copyfile(dict["source_path"] + dict["file_name"],
                                dict["destination_path"] + dict["file_name"])

    except IOError as e:
        print(e)

