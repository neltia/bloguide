from fastapi import FastAPI
from app.admin import container_controller
from app.alert import email_controller
from app.tool import calc_controller
from app.markdown import blog_controller as markdown_blog
from app.analysis import blog_controller as analysis_blog
from app.stat import blog_controller as stat_blog

app = FastAPI()

app.include_router(container_controller.router, prefix="/admin/container", tags=["Admin Container"])
app.include_router(email_controller.router, prefix="/alert/email", tags=["Alert Email"])
app.include_router(calc_controller.router, prefix="/tool/calc", tags=["Tool Calc"])
app.include_router(markdown_blog.router, prefix="/markdown/blog", tags=["Markdown Blog"])
app.include_router(analysis_blog.router, prefix="/analysis/blog", tags=["Analysis Blog"])
app.include_router(stat_blog.router, prefix="/stat/blog", tags=["Stat Blog"])
