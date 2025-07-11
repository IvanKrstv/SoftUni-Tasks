from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id: int):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id: int):
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join(repr(doc) for doc in self.documents)


    def __edit_object(self, object_id, object_collection, *args):
        obj = self.__find_object(object_id, object_collection)
        if obj:
            obj.edit(*args)

    def __delete_object(self, object_id: int, object_collection: list):
        obj = self.__find_object(object_id, object_collection)
        if obj:
            object_collection.remove(obj)

    @staticmethod
    def __find_object(object_id, object_collection):
        return next((el for el in object_collection if el.id == object_id), None)


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
