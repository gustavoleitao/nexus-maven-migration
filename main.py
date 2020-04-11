
import search_dependencies
import upload_to_nexus
import urllib3
import local_log
from getpass import getpass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_path = input("Enter the local path dependencies: ")
url = input("Nexus URL: ")
repository = input("Repository name: ")
user = input("Nexus user: ")
password = getpass("Nexus password: ")

if not url.endswith("/"):
    url = url + '/'

nexusApi = url + 'service/rest/v1/components'

local_log.log(f"Listing dependencies at {base_path}")
dependencies = search_dependencies.list_folder_recursively(base_path)
local_log.log(f"It was found {len(dependencies)} valid dependencies. Lets begin the upload process.")

processed = 0
total = len(dependencies)
success = 0
errors = 0

local_log.log('Uploading...')

for dependency in dependencies:
    result = upload_to_nexus.upload_dependency(dependency, url=nexusApi, user=user, password=password,
                                               repository=repository)
    processed += 1
    if result.get('code') != 204:
        errors += 1
        local_log.log(f"Fail to upload the dependency ${dependency}.")
    else:
        success += 1
    if processed % 10 == 0:
        local_log.log(
            f"Progress {(processed / float(total)) * 100}%. Total processed: {processed} with {success} success and {errors} errors.")

if errors > 0:
    local_log.log(
        f"Finished! {processed} dependencies were processed with {success} success and {errors} errors. "
        f"The details can be found in /logs.")
else:
    local_log.log(f"Finished! {processed} dependencies were processed with {success} success and {errors} errors")
