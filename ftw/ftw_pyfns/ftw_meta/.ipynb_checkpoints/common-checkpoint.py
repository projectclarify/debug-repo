# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Objects shared across multiple functions."""


def require_admin_auth(func):
  # TODO
  pass


class User(object):
  def __init__(self, uid=None):
    self.uid = uid


class Context(object):
  def __init__(self, response_headers={}, user=User()):
    self.response_headers = response_headers
    self.user = user


def require_user_auth(func):
    def wrapper_require_user_auth(request):

        # The require_user_auth always wraps functions that
        # operate on request objects.
        ctx = Context()

        #allow_origin = "https://demo.cl4rify.org"
        allow_origin = "*"
        if request.method == 'OPTIONS':
            headers = {
                'Access-Control-Allow-Origin': allow_origin,
                'Access-Control-Allow-Methods': 'POST',
                'Access-Control-Allow-Headers': 'Authorization',
                'Access-Control-Max-Age': '3600',
                'Access-Control-Allow-Credentials': 'true'
            }

            return ('', 204, headers)

        # Set CORS headers for main requests
        headers = {
            'Access-Control-Allow-Origin': allow_origin,
            'Access-Control-Allow-Credentials': 'true'
        }
        ctx.response_headers = headers

        # ----------
        # TODO: Use firebase admin to verify the requester not
        # only has *an* auth token but is a registered user.
        # Write this information to response_partial
        # ----------

        data = {} # TODO: Get data from admin api
        # Pass information from data into ctx

        # Dev
        authorized = False

        if not authorized:
          return ('', 403, headers)

        # Use the further check of whether a user is auth. to
        # either directly return a not authorized response or
        # construct a context and pass that to a function call.

        return func(request, ctx)
    return wrapper_require_user_auth
