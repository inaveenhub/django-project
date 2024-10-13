# Multi-stage Docker buildfile
# See https://docs.docker.com/build/guide/multi-stage/

# Stage 1: Build the python dependencies
FROM python:3.12.7-slim-bookworm as build-python

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential libpq-dev

# ================================================

RUN mkdir -p /home/app/app-name

COPY ./requirements.txt /home/app/app-name/
RUN --mount=type=cache,target=/root/.cache \
    pip wheel --no-deps --wheel-dir /wheels \
    -r /home/app/app-name/requirements.txt

WORKDIR /home/app/app-name
COPY ./ /home/app/app-name

# ================================================
# Stage 2: Build the final image
# This copies the python dependencies from the first stage
# and the front end files from the second stage.
FROM python:3.12.7-slim-bookworm
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update \
    && apt-get install -y \
    curl \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

RUN addgroup --system django && adduser --system --ingroup django django

# ===============================================

COPY --from=build-python /wheels /wheels
COPY ./requirements.txt /home/app/app-name/
RUN --mount=type=cache,target=/root/.cache \
    pip install --no-index --find-links=/wheels \
    -r /home/app/app-name/requirements.txt \
    && rm -rf /wheels

WORKDIR /home/app/app-name

COPY --chown=django:django . /home/app/app-name

# ===============================================

# collect static files for whitenoise
RUN DEBUG=False python /home/app/app-name/manage.py collectstatic --noinput
RUN chown django:django -R static_root

USER django

COPY --chown=django:django config/docker_startup.sh /start
RUN chmod +x /start
CMD /start