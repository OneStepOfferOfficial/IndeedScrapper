# coding:utf-8

from flask import Blueprint, render_template, redirect, request, url_for, \
    session, jsonify

from app.models import db, Users
from app.utils import judgemember
from app.models import Permissions
from app.common.permission_required import permission_required

user = Blueprint('user', __name__)


@user.route('/register', methods=['POST', 'GET'])
def register():
    """
    注册接口
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']

        errors = judgemember(name, email)
        if password != repassword:
            errors.append('两次密码输入不一致')
        if len(errors) > 0:
            return render_template('register.html', errors=errors)
        else:
            user = Users(name, email, password)
            db.session.add(user)
            db.session.commit()
            db.session.close()
            return redirect(url_for('views.home'))
    else:
        return render_template('register.html')


@user.route('/login', methods=['POST', 'GET'])
def login():
    """
    登录接口
    """
    if request.method == 'POST':
        name = request.json['name']
        password = request.json['password']
        if name and password:
            current_user = db.session.query(Users).filter_by(name=name).first()
            if current_user:
                user_id = current_user.id
                session['user_id'] = user_id
                ret_data = dict(code=0, ret_msg="login success")
            else:
                ret_data = dict(code=1, ret_msg='user name or password is wrong')
        else:
            ret_data = dict(code=1, ret_msg='please input user_name or password')
    else:
        ret_data = dict(code=0, ret_msg='please login')

    return jsonify(ret_data)
    # errors = []
    # if request.method == 'POST':
    #     name = request.form['name']
    #     password = request.form['password']
    #     if name and password:
    #         current_user = db.session.query(Users).filter_by(name=name).first()
    #         if current_user:
    #             user_id = current_user.id
    #             session['user_id'] = user_id
    #             return redirect(url_for('views.home'))
    #         else:
    #             errors.append('user name or password is wrong')
    #     else:
    #         errors.append('please input user_name or password')

    # return render_template("login.html", errors=errors)


@user.route('/user-manage', methods=['POST', 'GET'])
@permission_required(Permissions.USER_MANAGE)
def user_manage():
    """
    用户管理
    """
    if request.method == 'POST':
        ret_data = dict(code=0, ret_msg='user manage')
    else:
        ret_data = dict(code=0, ret_msg='user list')
    return jsonify(ret_data)


@user.route('/merchant-manage', methods=['POST', 'GET'])
@permission_required(Permissions.MERCHANT_MANAGE)
def merchant_manage():
    """
    商家管理
    """
    if request.method == 'POST':
        ret_data = dict(code=0, ret_msg='merchant manage')
    else:
        ret_data = dict(code=0, ret_msg='merchant list')
    return jsonify(ret_data)


@user.route('/permission-manage', methods=['POST', 'GET'])
@permission_required(Permissions.UPDATE_PERMISSION)
def permission_manage():
    """
    权限管理
    """
    if request.method == 'POST':
        ret_data = dict(code=0, ret_msg='permission manage')
    else:
        ret_data = dict(code=0, ret_msg='permission list')
    return jsonify(ret_data)
