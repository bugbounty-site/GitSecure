from flask import render_template, flash, redirect, url_for, session, send_file, abort
from flask_login import login_required, login_user, current_user
from . import admin
from .. import document, db
from ..models import User, PassResets

import uuid

# function to check if user is verified
def check_admin():
	if not current_user.id == 1:
		abort(403)

@admin.route('/admin/users')
@login_required
def users():
	check_admin()
	users = User.query.all()
	return render_template('admin/users.html', users=users)


@admin.route('/admin/verify/<string:id>', methods=['GET','POST'])
@login_required
def verify_users(id):
	check_admin()
	user = User.query.get(id)
	if user.is_verified == 0:
		user.is_verified = 1
		user.balance = 5000
		db.session.commit()
	else:
		flash("This user is already verified. What are you doing?")
	return redirect(url_for('admin.users'))

@admin.route('/admin/lock/<string:id>', methods=['GET'])
@login_required
def lock_account(id):
	check_admin
	user = User.query.get(id)
	user.is_verified = 0
	db.session.commit()
	return redirect(url_for('admin.users'))
