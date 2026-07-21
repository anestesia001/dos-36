#!/usr/bin/env bash
set -euo pipefail

environment="${1:-}"
action="${2:-}"
prj_dir="/var/www/atech"
deploy_user="deployer"

case "$environment" in
  dev)
    server="10.129.0.10"
  ;;
  prod)
    server="10.129.0.5"
  ;;
  *)
    echo "Usage: $0 {dev|prod}"
    exit 1
  ;;
esac

case "$action" in
  deploy)
    repo="https://github.com/anestesia-tech/anestesia-tech-landing.git"
    release="release-$(date +%s)"
    echo "Start deploy to $environment ($server)..."
    ssh -o StrictHostKeyChecking=no "${deploy_user}"@"${server}" bash <<EOF
    git clone "$repo" "$prj_dir"/"$release"
    cd "$prj_dir"
    ln -sfn "$release" current
EOF
  ;;
   rollback)
    ssh -o StrictHostKeyChecking=no "${deploy_user}"@"${server}" PRJ_DIR="$prj_dir" bash <<'EOF'
    set -euo pipefail
    releases=$(find "$PRJ_DIR" -maxdepth 1 -type d -name "release*")
    echo "Current release is $(stat ${PRJ_DIR}/current | awk -F: 'NR==1{print $2}')"
    echo -e "All releases:\n$releases"
EOF
    read -r -p "Choose release to rollback: " release_old
    ssh -o StrictHostKeyChecking=no "${deploy_user}@${server}" PRJ_DIR="$prj_dir" bash <<'EOF'
    cd $PRJ_DIR
    ln -sfn $release_old current
EOF
  ;;
  *) echo "Usage: $0 {dev|prod} {deploy|rollback}"
  ;;
esac
