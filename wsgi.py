# -*- coding: utf-8 -*-
"""
WSGI 入口文件 - Render 部署使用
"""
import os
from app import create_app

# 创建 Flask 应用实例
app = create_app()

if __name__ == '__main__':
    app.run()
