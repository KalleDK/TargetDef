from conans import ConanFile, CMake, tools


class TargetdefConan(ConanFile):
    name = "TargetDef"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/kalledk"
    description = "Demo Lib"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "target": ["A", "B"]}
    default_options = "shared=True", "target=A"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["targetdef"]
