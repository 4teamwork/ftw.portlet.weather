from ftw.upgrade import UpgradeStep


class UpdateWeatherWidgetURL(UpgradeStep):
    """Update weather widget url.
    """

    def __call__(self):
        self.install_upgrade_profile()
