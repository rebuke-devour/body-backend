""" A BodyController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Body import Body

class BodyController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BodyController)
        """
        id = self.request.param("id")
        return Body.find(id)
        

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BodyController)
        """
        return Body.all()
      

    def create(self):
        name = self.request.input("name")
        date_discovered = self.request.input("date_discovered")
        details = self.request.input("details")

        body= Body.create({ "name": name, "date_discovered": date_discovered, "details": details })
        return body

      
    def update(self):
        id = self.request.param("id")
        name = self.request.input("name")
        date_discovered = self.request.input("date_discovered")
        details = self.request.input("details")
        
        Body.where("id", id).update({"name": name, "date_discovered": date_discovered, "details": details})
        return Body

    def destroy(self):
        id = self.request.param("id")
        body = Body.where("id", id).get()
        Body.where("id", id).delete()
        return body