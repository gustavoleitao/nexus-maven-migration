import os


def list_folder_recursively(path, dependencies=[]):
    dependency = {}
    for entry in os.listdir(path):

        item = os.path.join(path, entry)
        list_dir = [os.path.isfile(item) for f in os.listdir('.')]

        if all(list_dir) and os.path.isfile(item):
            if (item.endswith('.pom')):
                dependency['pom'] = item
            elif (item.endswith('-sources.jar')):
                dependency['sources'] = item
            elif (item.endswith('-javadoc.jar')):
                dependency['javadoc'] = item
            elif  (not item.endswith('-jar-with-dependencies.jar')) and item.endswith('.jar'):
                dependency['artifact'] = item
                dependency['artifact.ext'] = "jar"
            elif (not item.endswith('-jar-with-dependencies.jar')) and item.endswith('.war'):
                dependency['artifact'] = item
                dependency['artifact.ext'] = "war"

        if os.path.isdir(item):
            list_folder_recursively(item, dependencies)

    if "artifact" in dependency:
        dependencies.append(dependency)

    return dependencies
