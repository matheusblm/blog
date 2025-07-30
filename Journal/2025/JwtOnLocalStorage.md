LocalStorage was never meant to be used as secure storage

LocalStorage is a place to to store any information in the users browser

Cookeis have a small storage size compare a localStorage

LocalStorage (5mb) x Cookies (4kb)

Bad things about Local Storage -

1. Synchronous - each local storage operation will be run once at a time, for complex applications it will slow down the apps run time.
2. String Storage Only.
3. Limit Storage (5mb across all major browser)
4. Incompatible with web workers - Can be with a chrome extension, is not an option at all as web workers do not have access to it.
5. Security Permissions - Any Javascript code on your page can access local storage, it has no data protection.

"Storing in local storage any sensitive information is equivalent to posting on Twitter or Instagram that information."

When use sensitive information in local storage, you open yourself to cross-site-scripting attacks.


Do not use every library you see on the internet
Do not store anything even remotely important in local storage


The most problem its used a third part libary with some malicious content