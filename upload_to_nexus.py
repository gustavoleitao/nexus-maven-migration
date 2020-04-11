import requests

def uploadDependency(dependency,  url, user, password, repository='maven-releases'):

    if len(dependency) < 2:
        return {'code': 0, 'msg': 'Dependência inválida. Deve possuir pelo menos o POM e o artefato.'}

    params = (
        ('repository', repository),
    )

    files = {
        'maven2.generate-pom': (None, 'false')
    }

    asset = 0

    if "artifact" in dependency:
        asset += 1
        files[f"maven2.asset{asset}"] = (dependency.get('artifact'), open(dependency.get('artifact'), 'rb'))
        files[f"maven2.asset{asset}.extension"] = (None, dependency.get('artifact.ext'))

    if "pom" in dependency:
        asset += 1
        files[f"maven2.asset{asset}"] = (dependency.get('pom'), open(dependency.get('pom'), 'rb'))
        files[f"maven2.asset{asset}.extension"] = (None, 'pom')

    if "sources" in dependency:
        asset += 1
        files[f"maven2.asset{asset}"] = (dependency.get('sources'), open(dependency.get('sources'), 'rb'))
        files[f"maven2.asset{asset}.extension"] = (None, 'jar')
        files[f"maven2.asset{asset}.classifier"] = (None, 'sources')

    if "javadoc" in dependency:
        asset += 1
        files[f"maven2.asset{asset}"] = (dependency.get('javadoc'), open(dependency.get('javadoc'), 'rb'))
        files[f"maven2.asset{asset}.extension"] = (None, 'jar')
        files[f"maven2.asset{asset}.classifier"] = (None, 'javadoc')

    result =  requests.post(url, params=params, auth=(user, password), files=files, verify=False)

    return {'code': result.status_code, 'msg': result.text}