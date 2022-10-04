
(cl:in-package :asdf)

(defsystem "art_publisher-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "body" :depends-on ("_package_body"))
    (:file "_package_body" :depends-on ("_package"))
    (:file "marker" :depends-on ("_package_marker"))
    (:file "_package_marker" :depends-on ("_package"))
  ))