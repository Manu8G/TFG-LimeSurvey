import logging
import git
import os
actual_path = os.path.abspath(__file__)
repo = git.Repo(search_parent_directories=True, path=actual_path)
path_repo = repo.git.rev_parse("--show-toplevel")
