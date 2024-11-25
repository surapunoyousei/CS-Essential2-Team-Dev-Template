from rest_framework import viewsets, routers
from app.models import User_Model
from .serializers import UserSerializer

class UserApi(viewsets.ModelViewSet):
    queryset = User_Model.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User_Model.objects.all()
        L_id = self.request.query_params.get('id')
		# queryでidを受けるとidでDBに検索をかけるようにしている。

        if L_id:
            queryset = queryset.filter(user_id=L_id)
        return queryset

router = routers.DefaultRouter()
router.register(r'user', UserApi)
