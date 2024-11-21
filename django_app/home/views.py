from rest_framework.decorators import api_view
from rest_framework.response import Response
from .task import analyse_repo_task 
from celery.result import AsyncResult

@api_view(['POST'])
def start_task(request):
   data = request.data
   repo_url = data.get('repo_url')
   pr_number = data.get('pr_number')
   github_token = data.get('github_token')
   task = analyse_repo_task.delay(repo_url,pr_number,github_token)

   return Response({
      "task_id" : task.id,
      "status"  : "Task started"
    })
  
@api_view(['GET'])
def task_status_view(request, task_id):
    print(f"GET request received for Task ID: {task_id}")
    
    result = AsyncResult(task_id)
    
    print(f"Task State: {result.state}")
    
    response = {
        "task_id": task_id,
        "status": result.state,
    }

    if result.state == "SUCCESS":
        response["result"] = result.result
    elif result.state == "PENDING":
        response["result"] = "Task is still processing."
    elif result.state == "FAILURE":
        response["result"] = str(result.result)
    else:
        response["result"] = "No result available yet."
    
    print(f"Response: {response}")
    return Response(response)
