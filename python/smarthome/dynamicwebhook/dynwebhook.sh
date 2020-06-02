#!/bin/sh

hook=$1
echo "called $0 with param: $hook"
  case $hook in
        dummy)
                echo "called if param contains string dummy"
                ;;
        *)
                # this will always be invoked
                ;;
  esac

