#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5f39ce86-615d-4cb6-8723-a0f4d379c42f")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "pM^4VlqeT7s%BK5P.veTh:ou")
