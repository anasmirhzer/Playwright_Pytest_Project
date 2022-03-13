class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://127.0.0.1:8081")

    Menu_homepage_button = "id=openbtn"
    Menu_Homepage_prevention_button = "#mySidepanel >> text=Prévention"
    Menu_Homepage_Formation_button = "#mySidepanel >> text=Formation"
    Menu_Homepage_Qualite_button = "#mySidepanel >> text=Qualité"
    Homepage_me_contacter_button = "id=contact-button-container"
    Homepage_legend_p = "div.section.section-grise1 > p"
    Homepage_logo_img = "div.cover > img"
    Homepage_brandname_text = "div.cover > img"
    Homepage_title_text = "body > div.cover > h1"
    Homepage_formations_link = "text=Formations"
    Homepage_prevention_link = "text=Prévention"
    Homepage_qualite_link = "text=Qualité"
    Homepage_domaines_text = "div.section.section-grise2 > h2"

    def check_homepage_elements(self):
        assert self.page.is_visible(HomePage.Homepage_me_contacter_button)
        assert self.page.is_visible(HomePage.Homepage_logo_img)
        assert self.page.is_visible(HomePage.Homepage_title_text)
        assert self.page.is_visible(HomePage.Homepage_logo_img)
        assert self.page.is_visible(HomePage.Homepage_brandname_text)
        assert self.page.is_visible(HomePage.Homepage_formations_link)
        assert self.page.is_visible(HomePage.Homepage_prevention_link)
        assert self.page.is_visible(HomePage.Homepage_qualite_link)
        assert self.page.is_visible(HomePage.Homepage_domaines_text)
        assert self.page.is_visible(HomePage.Homepage_legend_p)

    def check_homepage_menu_elements(self):
        self.page.locator(HomePage.Menu_homepage_button).click()
        assert self.page.is_visible(HomePage.Menu_Homepage_prevention_button)
        assert self.page.is_visible(HomePage.Menu_Homepage_Formation_button)
        assert self.page.is_visible(HomePage.Menu_Homepage_Qualite_button)
