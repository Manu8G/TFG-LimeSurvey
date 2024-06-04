from repository.admin_repository import AdminRepository
# from dto.survery import Survery

class AdminService():

    repository = AdminRepository()

    def create_survery(self, data: dict):
        try:
            data = self.repository.create_survery(data=data)
            
            # return SurveryResponse(data= data.data, usuario=data.user)
        except Exception as e:
            raise RuntimeError(str(e))