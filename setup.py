from setuptools import setup

setup(
	name="opentelemetry-autoconf",
	version="0.1",
	description="opentelemetry autoconf",
	py_modules=["opentelemetry_autoconf"],
	packages=[""],
	package_data={"":["opentelemetry_autoconf.pth"]},
	install_requires=[
		"opentelemetry-sdk",
	],
	extras_require = {
		"jaeger": ["opentelemetry-exporter-jaeger"]
	}
)
