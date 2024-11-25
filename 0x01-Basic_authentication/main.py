#!/usr/bin/bash
curl "http://0.0.0.0:5000/api/v1/status" && curl "http://0.0.0.0:5000/api/v1/status/" && curl "http://0.0.0.0:5000/api/v1/users" && curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test" && curl "http://0.0.0.0:5000/api/v1/unauthorized" && curl "http://0.0.0.0:5000/api/v1/forbidden"
