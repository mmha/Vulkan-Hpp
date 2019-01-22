from conans import ConanFile, tools, CMake
import os


class VulkanHppConan(ConanFile):
    name = "vulkan-hpp"
    version = "1.1.98"
    requires = "vulkan-headers/[>=1.1.98]@mmha/testing"
    settings = "os", "compiler", "arch", "build_type"
    description = " Open-Source Vulkan C++ API"
    url = "https://github.com/KhronosGroup/Vulkan-Hpp"
    exports_sources= "*", "!.git"
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.run("./VulkanHppGenerator")

    def package(self):
        self.copy("*.hpp", dst="include/vulkan", src="vulkan")

    def package_id(self):
        self.info.header_only()
