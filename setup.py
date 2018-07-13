from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='UKPostCode',
      version='0.1',
      description = 'Validate UK post code and format it',
      classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3,6.3',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='post postcode ukpostcode uk',
      url='http://github.com/dhanya1/UKPostCodeValidationa',
      author='Dhanya Jaychandra',
      author_email='dhanyasj01@gmail.com',
      license='MIT',
      packages=['UKPostCode'],
      include_package_data=True,
      zip_safe=False)
