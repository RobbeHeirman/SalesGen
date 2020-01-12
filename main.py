import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from DatabaseReader import DatabaseReader

kivy.require('1.0.6')  # replace with your current kivy version !

from kivy.app import App


db = DatabaseReader()


class ListBox(RecycleView):
    def __init__(self, **kwargs):
        super(ListBox, self).__init__(**kwargs)
        self.data = [{'text': str(x.name)} for x in db.get_vendor_names()]


class BaseWidget(BoxLayout):
    pass


class SalesApp(App):

    def build(self):
        return BaseWidget()


if __name__ == '__main__':
    print([{'text': str(x)} for x in db.get_vendor_names()])
    SalesApp().run()
