from flask_restx import Resource


class ContainerResource(Resource):
    def get(self):
        return {'message': 'Docker operations 1'}

    def post(self):
        return {'message': 'Create a new Docker container 1'}


class ContainerActionResource(Resource):
    def get(selt):
        return {'message': 'Docker operations 2'}

    def post(self):
        return {'message': 'Create a new Docker container 2'}
