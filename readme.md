# [unofficial] lm-logs-sdk-python (beta)
Python SDK for sending logs to LogicMonitor

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=ncloc)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=bugs)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=security_rating)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=sqale_index)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=dewhurstwill_lm-logs-sdk-python&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=dewhurstwill_lm-logs-sdk-python)

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
