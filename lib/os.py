import os

class Os_Utils:
    """
    A class that provides utilities for interacting with the operating system.

    Attributes:

    """




    path: str = os.get_cwd()

    @property
    def get_cwd() -> str:
        """
        Get the current working directory.

        Returns:
            str: The current working directory.
        """
        return os.getcwd()

    def get_username() -> str:
        """
        Get the username of the current user.
        
        Returns:
            str: The username of the current user.
        """
        return os.getlogin().split("@")[0]


    def ls(self) -> list[str]:
        """
        List the files and directories in the current directory.

        Args:
            path (str): The path of the directory to list.
        Returns:
            list[str]: A list of files and directories in the current directory.
        """
        return os.listdir(self.path)

    def mkdir(dir: str) -> None:
        """
        Create a directory at the specified path.
        
        Args:
            dir (str): The path of the directory to create.
        """
        os.mkdir(dir)

    def rmdir(self) -> None:
        """
        Remove a directory at the specified path.

        Args:
            path (str): The path of the directory to remove.
        """
        os.rmdir(self.path)

    def rm(self) -> None:
        """
        Remove a file at the specified path.

        Args:
            path (str): The path of the file to remove.
        """
        os.remove(self.path)

    def mv(src: str, dst: str) -> None:
        """
        Move a file or directory from the source path to the destination path.

        Args:
            src (str): The source path of the file or directory to move.
            dst (str): The destination path of the file or directory to move.
        """
        os.rename(src, dst)

    def cp(src, dst):
        """
        Copy a file from the source path to the destination path.

        Args:
            src (str): The source path of the file to copy.
            dst (str): The destination path of the file to copy.
        """

        if not os.path.exists(src):
            raise FileNotFoundError
        if not os.access(src, os.R_OK):
            raise PermissionError
        if os.path.isdir(src):
            raise ValueError("Source is a directory.")
        if os.path.isdir(dst):
            raise ValueError("Destination is a directory.")
        


        with open(src, 'rb') as f:
            data = f.read()
        with open(dst, 'wb') as f:
            f.write(data)

class FileNotFoundError(Exception):
    raise Exception("File not found.")

class DirectoryNotFoundError(Exception):
    raise Exception("Directory not found.")

class PermissionError(Exception):
    raise Exception("Permission denied.")


