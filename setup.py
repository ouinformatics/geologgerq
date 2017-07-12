#import ez_setup
#ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(name='geologgerq',
      version='0.0.19',
      packages= find_packages(),
      install_requires=[
          'celery==3.1.22',
          'pymongo==3.2.1',
          'requests==2.9.1',
          'ordereddict==1.1',
          'geojson==1.0.1',
          'anyjson==0.3.3',
          'billiard==2.7.3.12',
          'amqplib==1.0.2',
          'pandas',
          'kombu==2.3.2',
      ],
)

