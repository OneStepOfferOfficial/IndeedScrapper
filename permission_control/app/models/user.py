# coding:utf-8
"""
desc: 用户相关表模型
"""
from passlib.hash import bcrypt_sha256
from . import db


class Users(db.Model):
    """
    用户表
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer)

    def __init__(self, name, email, password, role = "user"):
        self.name = name
        self.email = email
        self.password = bcrypt_sha256.encrypt(str(password))
        # default role is "user"
        if role == "merchant":
            self.role_id = 2
        elif role == "admin":
            self.role_id = 3
        else:
            self.role_id = 1


class Permissions:
    """
    权限类
    """
    USER_MANAGE = 0X01
    MERCHANT_MANAGE = 0X02
    UPDATE_PERMISSION = 0X04


class Role(db.Model):
    """
    角色表
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    permissions = db.Column(db.Integer)

    @staticmethod
    # create/reset all the necessary roles and update their permissions
    def init_role():
        role_name_list = ['user', 'merchant', 'admin']
        roles_permission_map = {
            'user': [Permissions.USER_MANAGE],
            'merchant': [Permissions.MERCHANT_MANAGE],
            'admin': [Permissions.USER_MANAGE, Permissions.MERCHANT_MANAGE, Permissions.UPDATE_PERMISSION]
        }
        try:
            for role_name in role_name_list:
                role = Role.query.filter_by(name=role_name).first()
                if role is None:
                    role = Role(name=role_name)
                role.reset_permissions()
                for permission in roles_permission_map[role_name]:
                    role.add_permission(permission)
                db.session.add(role)
            db.session.commit()
        except:
            db.session.rollback()
        db.session.close()

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, permission):
        return self.permissions & permission == permission

    def add_permission(self, permission):
        if not self.has_permission(permission):
            self.permissions |= permission
