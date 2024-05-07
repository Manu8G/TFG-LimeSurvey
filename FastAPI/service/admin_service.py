from repository.admin_repository import AdminRespository
from dto.survery import Survery

class AdminService():

    repository = AdminRespository()

    def create_survery(self, data: Survery):
        try:
            data = self.repository.create_survery(data=data)
            
            return SurveryResponse(data= data.data, usuario=data.user)
        except Exception as e:
            raise RuntimeError(str(e))