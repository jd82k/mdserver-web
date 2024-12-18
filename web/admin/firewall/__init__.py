# coding:utf-8

# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------


from flask import Blueprint, render_template
from flask import request

from admin.user_login_check import panel_login_required
from admin.model import db, Firewall


from utils.firewall import Firewall as MwFirewall

import core.mw as mw

blueprint = Blueprint('firewall', __name__, url_prefix='/firewall', template_folder='../../templates/default')
@blueprint.route('/index', endpoint='index')
@panel_login_required
def index():
    return render_template('firewall.html')


# 防火墙列表
@blueprint.route('/get_list', endpoint='get_list', methods=['POST'])
@panel_login_required
def get_list():
    p = request.form.get('p', '1').strip()
    limit = request.form.get('limit', '10').strip()

    count = Firewall.query.filter_by().count()
    pagination = Firewall.query.filter_by().paginate(page=int(p), per_page=int(limit))
  
    rows = []
    for item in pagination.items:
        t = {}
        t['id'] = item.id
        t['port'] = item.port
        t['protocol'] = item.protocol
        t['ps'] = item.ps
        t['add_time'] = item.add_time
        t['update_time'] = item.update_time
        rows.append(t)

    data = {}
    data['data'] = rows
    data['page'] = mw.getPage({'count':count,'tojs':'getLogs','p':p,'row':limit})
    return data

# 获取站点日志目录
@blueprint.route('/get_www_path', endpoint='get_www_path', methods=['POST'])
@panel_login_required
def get_www_path():
    path = mw.getLogsDir()
    return {'path': path}

# 获取ssh信息
@blueprint.route('/get_ssh_info', endpoint='get_ssh_info', methods=['POST'])
@panel_login_required
def get_ssh_info():
    mf = MwFirewall.instance()
    return mf.getSshInfo()


# 切换ping开关
@blueprint.route('/set_ping', endpoint='set_ping', methods=['POST'])
@panel_login_required
def set_ping():
    mf = MwFirewall.instance()
    return mf.setPing()








