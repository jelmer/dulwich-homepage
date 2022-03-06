FROM debian:sid-slim
ADD . /code
RUN apt -y update && apt -y install python3-fastimport python3-paramiko pydoctor rsync git pelican make python3-webassets python3-sphinx python3-typogrify python3-pygments python3-markdown python3-pip && python3 -m pip install pelican-sitemap git+https://github.com/jelmer/googleanalytics && cd /code && make -C /code publish && git clone https://github.com/dulwich/dulwich /code/dulwich && make -C /code/dulwich doc apidocs && rsync -az /code/dulwich/docs/build/html/ /code/output/docs && rsync -az /code/dulwich/apidocs/ /code/output/apidocs/ && apt -y purge pelican python3-typogrify python3-pygments python3-markdown && apt -y autoremove
RUN apt -y install node-static
EXPOSE 8080
CMD node /usr/bin/node-static -a 0.0.0.0 /code/output
