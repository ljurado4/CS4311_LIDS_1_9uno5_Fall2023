
# Application Security and Development Security Technical Implementation Guide

## | ID | Description | Mitigating Reason |
## | --- | --- | --- |
1. | V-222400 | Validity periods must be verified on all application messages using WS-Security or SAML assertions. | Not Applicable; Our implementation does not contain SOAP Capabilities.|

2. | V-222404 | The application must use both the NotBefore and NotOnOrAfter elements or OneTimeUse element when using the Conditions element in a SAML assertion. | Not Applicable; as our implementation does not handle SAML assertions.|

3. | V-222612 | The application must not be vulnerable to overflow attacks. | Not Applicable; our implementation uses a memory-safe language.|

4. | V-222578 | The application must destroy the session ID value and/or cookie on logoff or browser close. | Not Applicable; Our project does not utilize sessions or cookies for user authentication or session management.|

5. | V-222430 | The application must execute without excessive account permissions. | Not Applicable; Our implementation does not require any type of permissions.|

6. | V-222432 The application must enforce the limit of three consecutive invalid logon attempts by a user during a 15 minute time period. | Not applicable; our system doesn’t require login credentials.| 

7. | V-222577 | The application must not expose session IDs. | Not Applicable; Our implementation does not store session IDs.|

8. | V-222609 | The application must not be subject to input handling vulnerabilities. | Applicable; our implementation deals with common input handling vulnerabilities.|

9. | V-222608 | The application must not be vulnerable to XML-oriented attacks. | Applicable; our implementation validates the XML file against a defined schema, ensuring only well formed and schema compliant XML data is processed.|
 
10. | V-222602 | The application must protect from Cross-Site Scripting (XSS) vulnerabilities.|Applicable; as our current version, specific XSS protection mechanisms have not been implemented.|

11. | V-222601 | The application must not store sensitive information in hidden fields. | Not applicable; our implementation does not request any sensitive information from the user.|

12. | V-222607 | The application must not be vulnerable to SQL Injection. | Not applicable; our implementation does not interact with or manage a database.| 

13. | V-222604 | The application must protect from command injection. | Applicable; our implementation deals with common input handling vulnerabilities.|

14. | V-222403 | The application must use the NotOnOrAfter condition when using the SubjectConfirmation element in a SAML assertion. | Not applicable; the system doesn’t require any authentication or authorization data between domains.|

15. | V-222585 | The application must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. | Applicable, but not implemented; the development team is actively focused on preventing any limitations that could potentially impact functionality.|

16. | V-222550 | The application, when utilizing PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor. | Not applicable; our implementation does not require PKI authentication.|

17. | V-222522 | The application must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). | Not applicable; our implementation does not require any type of authentication.|

18. | V-222554 | The application must not display passwords/PINs as clear text. | Not applicable; our implementation does not ask or display any type of passwords/PINs.| 

19. | V-222596 | The application must protect the confidentiality and integrity of transmitted information. | Applicable; our implementation ensures the protection of the confidentiality and integrity of transmitted information.  Data transfers are conducted over encrypted channels using HTTPS.|

20. | V-222399 | Messages protected with WS_Security must use time stamps with creation and expiration times. | Not applicable; our implementation doesn’t require WS-Security for SOAP based web services.|

21. | V-222658 | All products must be supported by the vendor or the development team. | Applicable; our system has exclusively incorporated supported applications and has not included any unsupported ones.| 

22. | V-222659 | The application must be decommissioned when maintenance or support is no longer available. | Applicable; the unsupported software should be replaced.|

23. | V-222551 | The application, when using PKI-based authentication, must enforce authorized access to the corresponding private key. | Not Applicable; Our implementation does not require PKI authentication.|

24. | V-222620 | Application web servers must be on a separate network segment from the application and database servers if it is a tiered application operating in the DoD DMZ. | Applicable; the architecture of our implementation is designed with segregated network segments for web servers and application logic.|

25. | V-222536 | The application must enforce a minimum 15-character password length. | Not applicable; our system doesn’t require login credentials.|

26. | V-222643 | The application must have the capability to mark sensitive/classified output when required. | Applicable; but yet not implemented, currently our system does not include an explicit mechanism for marking sensitive or classified output.|

27. | V-222542 | The application must only store cryptographic representations of passwords. | Not applicable; our implementation does not require any passwords.|

28. | V-222543 | The application must transmit only cryptographically-protected passwords. | Not applicable; our implementation does not require any passwords.|

29. | V-222425 | The application must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. | Applicable, but not implemented; the development team is actively focused on preventing any limitations that could potentially impact functionality.| 

30. | V-222642 | The application must not contain embedded authentication data. | Not applicable; Our implementation does not require any authentication data.|

31. | V-222662 | Default passwords must be changed. | Not applicable; our implementation does not require  passwords.| 

32. | V-222555 | The application must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. | Not applicable; our implementation does not require any authentication data.|
## | --- | --- | --- |
