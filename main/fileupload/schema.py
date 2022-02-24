
from email import message
import graphene
from graphene_django import DjangoObjectType


from .models import FileUpload, Category
from graphene_file_upload.scalars import Upload
from django.conf import settings
import os

class FileInput(graphene.InputObjectType):
    name = graphene.String()
    type = graphene.Int()
    textNumber = graphene.String()
    releaseDate = graphene.String()
    expirationDate = graphene.String()
    description = graphene.String()
    internalNotes = graphene.String()

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'

class FileUploadType(DjangoObjectType):
    file = graphene.String()
    
    class Meta:
        model = FileUpload
        fields = '__all__'

    def resolve_file(self, info):
        if self.file:
            return "{}{}{}".format(settings.SITE_URL, settings.STATIC_URL, self.file)
        return None

def deleteFile(file):
    file_url = os.path.join(settings.MEDIA_ROOT, f"{file}")
    if os.path.isfile(file_url):
        os.unlink(file_url)


class CreateFileUpload(graphene.Mutation):
    file = graphene.Field(FileUploadType)
    class Arguments:
        data = FileInput(required=True)
        file = Upload(required=True)
        
    
    def mutate(root, info, file, data=None):
        file = FileUpload(
            file = file,
            name = data.name,
            type_id = data.type,
            text_number = data.textNumber,
            release_date = data.releaseDate,
            expiration_date = data.expirationDate,
            description = data.description,
            internal_notes = data.internalNotes,
        )
        file.save()
        return CreateFileUpload(file=file)

# update 
class UpdateFileUpload(graphene.Mutation):
    file = graphene.Field(FileUploadType)
   
    class Arguments:
        id = graphene.Int()
        data = FileInput(required=True)
        file = Upload()
    
    def mutate(root, info, id, data=None, file=None):
        file_instance = FileUpload.objects.get(id=id)
        
        if file_instance:
            if file:
               deleteFile(file_instance.file)

               file_instance.name = data.name
               file_instance.type_id = data.type
               file_instance.file = file
               file_instance.save()
            else:
               file_instance.name = data.name
               file_instance.type_id = data.type
               file_instance.save()
        else:
            return UpdateFileUpload(message=f"ID {id} not found")

        return UpdateFileUpload(file=file_instance)  

# delete
class DeleteFileUpload(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int()
    
    def mutate(root, info, id):

        file_instance = FileUpload.objects.get(id=id)
        if file_instance:

            deleteFile(file_instance.file)
            file_instance.delete()

            return DeleteFileUpload(message=f"ID {id} deleted")
        return DeleteFileUpload(message=f"ID {id} not found")


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    files = graphene.List(FileUploadType)
    file = graphene.Field(FileUploadType, id=graphene.Int(required=True))

    def resolve_categories(root, info):
        return Category.objects.all()

    def resolve_files(root, info):
        return FileUpload.objects.select_related('type').all()

    def resolve_file(root, info, id):
        try:
            return FileUpload.objects.get(id=id)
        except FileUpload.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):

    file_upload = CreateFileUpload.Field(description='create')
    file_update = UpdateFileUpload.Field(description='update')
    file_delete = DeleteFileUpload.Field(description='delete')