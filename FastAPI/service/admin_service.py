from repository.admin_repository import AdminRepository

class AdminService():

    repository = AdminRepository()

    def create_survery(self, data: dict):
        try:
            data = self.repository.create_survery(data=data)
            
        except Exception as e:
            raise RuntimeError(str(e))