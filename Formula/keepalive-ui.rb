class KeepaliveUi < Formula
  desc "Menu bar controller for the keepalive activity agent"
  homepage "https://github.com/skozar/keepalive"
  version "0.5.2"
  url "https://github.com/skozar/keepalive/releases/download/v0.5.2/KeepaliveUI-0.5.2.zip"
  sha256 "75235a07e0bc5135c3edb76f636e4e1d01fbf724a3e3fc896121e315b35ad85f"
  license "MIT"

  depends_on "keepalive"

  def install
    (prefix/"Keepalive.app").install Dir["*"]
  end

  def post_install
    app_source = prefix/"Keepalive.app"
    app_target = Pathname("/Applications/Keepalive.app")
    app_target.delete if app_target.exist? || app_target.symlink?
    app_target.make_symlink(app_source)
  end

  def caveats
    <<~EOS
      Keepalive.app has been symlinked to /Applications/Keepalive.app.
      Launch it from Spotlight or Launchpad.

      Settings are stored in ~/.config/keepalive/settings.json
      and survive reinstalls — you only need to configure once.

      IMPORTANT: The keepalive CLI binary must have Accessibility
      permission for mouse jiggle to work:
        System Settings → Privacy & Security → Accessibility
        Add: /opt/homebrew/bin/keepalive
    EOS
  end

  test do
    system "test", "-d", prefix/"Keepalive.app"
  end
end
