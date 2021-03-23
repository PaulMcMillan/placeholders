import io
import os
import sys
import tarfile

package_name = sys.argv[1]
package_version = "0.0.0a0"
if len(sys.argv) > 2:
    package_version = sys.argv[2]
package_info = f"""Metadata-Version: 1.2
Name: {package_name}
Version: {package_version}
Summary: Placeholder package to shadow internal names.
Home-page: https://github.com/paulmcmillan/placeholders
Author: Paul McMillan
Author-email: paul@mcmillan.ws
License: MIT
Description: This placeholder package exists to publicly claim an internal name, so that it cannot be used as part of a dependency confusion attack.
"""

path = f"{package_name}-{package_version}"
filename = f"{package_name}-{package_version}.tar.gz"
print(f"Creating new placeholder package:\n{filename}")

with tarfile.open(filename, "w:gz") as tar:
    data = package_info.encode("utf-8")
    info = tarfile.TarInfo(name=f"{path}/PKG-INFO")
    info.size = len(data)
    tar.addfile(tarinfo=info, fileobj=io.BytesIO(data))

upload = input("Upload to pypi? (y/n) ")
if upload.lower() in ['y', 'yes']:
    #os.system(f'twine upload --repository testpypi {filename}')
    os.system(f'twine upload --repository pypi {filename}')
