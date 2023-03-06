import web
from Models import RegisterModel, LoginModel, Posts


web.config.debug = False

# URLS
urls = (
    '/', 'Home',
    '/register', "Register",
    "/postregistration", "PostRegistration",
    "/login", "Login",
    "/check-login", "CheckLogin",
    "/logout", "Logout",
    "/post-activity", "PostActivity",
    "/profile", "Profile",
    "/update-profile", "UpdateProfile"
)

# initialize web.py
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={"user": None})
session_data = session._initializer
render = web.template.render("Views/Templates", base="MainLayout", globals={"session": session_data, "current_user": session_data["user"]})


# Class associated with the URLS
class Home:
    def GET(self):
        data = type('obj', (object,), {"username": "Leo", "password": "asd"})

        login = LoginModel.LoginModel()

        is_correct = login.check_user(data)

        if is_correct:
            session_data["user"] = is_correct

        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


# Register a new user
class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


# Check valid login
class CheckLogin:
    def POST(self):
        data = web.input()

        login = LoginModel.LoginModel()

        is_correct = login.check_user(data)

        if is_correct:
            session_data["user"] = is_correct
            return is_correct

        return "error"


# kills current session
class Logout:
    def GET(self):
        session["user"] = None
        session_data["user"] = None
        session.kill()
        return "success"


# post a new activity in blog
class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        post_model = Posts.Posts()
        post_model.insert_post(data)

        return "success"


class Profile:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts(session_data["user"]["username"])

        return render.Profile(posts, session_data["user"]["email"])


# Update user's personal data
class UpdateProfile:
    def POST(self):
        email = web.input()
        updated = None
        if email:
            login_model = LoginModel.LoginModel()
            updated = login_model.update_user(session_data["user"], email["email"])

            session_data["user"] = updated

        return updated


if __name__ == "__main__":
    app.run()
