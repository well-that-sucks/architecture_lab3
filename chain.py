from facade import *

class AbstractProcessor:
    next_processor = None
    facade = Facade()

    def set_next(self, processor):
        self.next_processor = processor
        return processor

    def process(self, request):
        pass

class GetProcessor(AbstractProcessor):
    def process(self, request):
        if request == 'GET':
            return {'items': self.facade.get()}
        else:
            if self.next_processor:
                return self.next_processor.process(request)
            return 'No matching processors'

class PostProcessor(AbstractProcessor):
    def process(self, request):
        if request == 'POST':
            self.facade.update()
            return 'Updated'
        else:
            if self.next_processor:
                return self.next_processor.process(request)
            return 'No matching processors'

class DeleteProcessor(AbstractProcessor):
    def process(self, request):
        if request == 'DELETE':
            self.facade.delete()
            return 'Deleted'
        else:
            if self.next_processor:
                return self.next_processor.process(request)
            return 'No matching processors'

class PutProcessor(AbstractProcessor):
    def process(self, request):
        if request == 'PUT':
            self.facade.insert()
            return 'Inserted'
        else:
            if self.next_processor:
                return self.next_processor.process(request)
            return 'No matching processors'