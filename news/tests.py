from django.test import TestCase
from .models import Editor

# Create your tests here.
class EditorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.yvon = Editor(first_name ='Yvonne', last_name = 'Ouma', email = 'yvonne@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.yvon,Editor)) 

    # testing Save method
    def test_save_method(self):
        self.yvon.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)  

    # def test_delete_method(self):
    #     self.yvon.delete_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)    


    