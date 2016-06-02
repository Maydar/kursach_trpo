def current_url(request):
    namespace = None
    if request.resolver_match is not None and len(request.resolver_match.namespaces) > 0:
        namespace = request.resolver_match.namespaces[0]

    return {
        'current_namespace': namespace,
        'current_url': request.resolver_match.url_name if request.resolver_match is not None else None
    }


def is_teacher(request):
    return  {
        'is_teacher': request.user.groups.filter(name='teacher').exists()
    }

def is_student(request):
    return {
        'is_student': request.user.groups.filter(name='student').exists()
    }
