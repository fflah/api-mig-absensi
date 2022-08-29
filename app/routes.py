from app import api, web
from app.controllers.api import ActivityController, AuthContoller, AbsensiController

# route for api auth
api.add_resource(AuthContoller.Register, '/register')
api.add_resource(AuthContoller.Login, '/login')
api.add_resource(AuthContoller.Refresh, '/refresh')

# route for absensi
api.add_resource(AbsensiController.Checkin, '/checkin')
api.add_resource(AbsensiController.Checkout, '/checkout')
api.add_resource(AbsensiController.RiwayatAbsensi, '/riwayat-absensi')

# route for activity
api.add_resource(ActivityController.Activity, '/activity', '/activity/<string:id>')
api.add_resource(ActivityController.ActivityFilterDate, '/activity-filter-date',)