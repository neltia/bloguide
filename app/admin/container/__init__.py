from flask_restx import Namespace
from .container_controller import ContainerResource, ContainerActionResource

# container 네임스페이스 생성
container_ns = Namespace('container', description='Container')

# 기본 경로 및 하위 경로에 대한 리소스 등록
container_ns.add_resource(ContainerResource, '/')
container_ns.add_resource(ContainerActionResource, '/<string:action>')
