import os

from conans import ConanFile, tools


class BoostdiConan(ConanFile):
    name = "boost-di"
    version = "1.1.0"
    license = "Boost Software License"
    author = "inexorgame info@inexor.org"
    url = "https://github.com/inexorgame/conan-boost-di"
    description = "Boost-Experimental Dependency Injection Library."
    topics = ("Dependency Injection", "DI", "Boost")
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        # self.run("git clone ...") or
        tools.download("https://github.com/boost-experimental/di/archive/v{}.zip".format(self.version), "file.zip")
        tools.unzip("file.zip" )

    def package(self):
        self.copy("*.hpp", dst="include", src=os.path.join("di-{}".format(self.version), "include"))

