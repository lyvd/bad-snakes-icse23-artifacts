import os
import subprocess

PATH_TO_PACKAGES = ""
PATTH_TO_RESULTS_DIR = ""
packages_dir = os.path.abspath(PATH_TO_PACKAGES)
results_dir = os.path.abspath(PATH_TO_RESULTS_DIR)

packages_path = [(f.name, f.path) for f in os.scandir(packages_dir) if f.is_dir()]
for package_name, package_path in packages_path:
        result_file = os.path.join(results_dir, f"{package_name}.json")
        if not os.path.exists(result_file):
            subprocess.run(["oss-detect-backdoor", "--format", "sarifv2", package_path, "-o", result_file])
            print(package_name, result_file)
