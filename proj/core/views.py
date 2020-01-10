from django.db import connections, DEFAULT_DB_ALIAS
from django.db.migrations.executor import MigrationExecutor
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from core.models import Item


def healthcheck(request):
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
    plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
    status = 503 if plan else 200
    return HttpResponse(status=status)


@method_decorator(csrf_exempt, name='dispatch')
class ItemsView(View):
    def get(self, request):
        qs = Item.objects.all()
        return JsonResponse({
            'qq': 'v6',
            'list': [
                {'id': obj.id, 'description': obj.description}
                for obj in qs]})

    def post(self, request):
        description = request.POST['description']
        Item.objects.create(description=description)
        return JsonResponse({'status': 'ok'})
