# lm-logs-sdk-python (beta)
Python SDK for sending logs to LogicMonitor

`pip install lm-logs-sdk-node` - if published

## Ingest:

### Required Environment Variables: 
- COMPANY_NAME
- ACCESS_ID
- ACCESS_KEY

``` python
import ingest from LMLogsSDKPython

ingest([{
    "message": "Hello! from Logic Monitor",
    "_lm.resourceId": {
        "<lm_property>": "<lm_property_value>"
    }
}]);

```